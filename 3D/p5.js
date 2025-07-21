let angleX = 0;
let angleY = 0;
let angleVX = 0.01;
let angleVY = 0.01;

let tubeRadius = 150;
let tubeHeight = 300;
let ball;
let gravity = 0.3;
let restitution = 0.6;
let friction = 0.99;

let polygon2D = [];

function setup() {
  createCanvas(600, 600, WEBGL);
  ball = new Ball();

  // 정오각형 꼭짓점 계산 (XZ 평면)
  let sides = 5;
  for (let i = 0; i < sides; i++) {
    let theta = TWO_PI * i / sides - PI / 2;
    let x = tubeRadius * cos(theta);
    let z = tubeRadius * sin(theta);
    polygon2D.push(createVector(x, z));
  }

  textFont('monospace', 14);
}

function draw() {
  background(20);
  directionalLight(255, 255, 255, 0.5, 1, -1);
  ambientLight(50);

  // 자동 회전
  angleX += angleVX;
  angleY += angleVY;

  rotateX(angleX);
  rotateY(angleY);

  drawPentagonalPrism();

  // 공은 회전 역변환 좌표계에서 처리
  push();
  rotateY(-angleY);
  rotateX(-angleX);
  ball.update();
  ball.display();
  pop();

  drawHUD();
}

function drawHUD() {
  resetMatrix();
  camera();
  fill(255);
  textAlign(LEFT, TOP);
  text(`
[마우스 드래그 → 회전 속도 조절]
W/S : 중력 ${gravity.toFixed(2)}
A/D : 탄성 ${restitution.toFixed(2)}
Q/E : 마찰 ${friction.toFixed(3)}
`, 10, 10);
}

function keyPressed() {
  if (key === 'W') gravity += 0.05;
  if (key === 'S') gravity = max(0, gravity - 0.05);
  if (key === 'A') restitution = max(0, restitution - 0.05);
  if (key === 'D') restitution = min(1, restitution + 0.05);
  if (key === 'Q') friction = min(1, friction + 0.005);
  if (key === 'E') friction = max(0.8, friction - 0.005);
}

// 마우스로 회전 속도 조절
let dragging = false;
let lastMouseX = 0;
let lastMouseY = 0;

function mousePressed() {
  lastMouseX = mouseX;
  lastMouseY = mouseY;
  dragging = true;
}

function mouseReleased() {
  dragging = false;
}

function mouseDragged() {
  if (dragging) {
    let dx = mouseX - lastMouseX;
    let dy = mouseY - lastMouseY;
    angleVY += dx * 0.0005;
    angleVX += dy * 0.0005;
    lastMouseX = mouseX;
    lastMouseY = mouseY;
  }
}

// 오각기둥 그리기
function drawPentagonalPrism() {
  noStroke();
  fill(100, 150, 255, 60); // 반투명 파란 벽

  let sides = 5;
  let r = tubeRadius;
  let h = tubeHeight / 2;

  let topPoints = [];
  let bottomPoints = [];

  for (let i = 0; i < sides; i++) {
    let theta = TWO_PI * i / sides - PI / 2;
    let x = r * cos(theta);
    let z = r * sin(theta);
    topPoints.push(createVector(x, -h, z));
    bottomPoints.push(createVector(x, h, z));
  }

  // 윗면
  beginShape();
  for (let v of topPoints) vertex(v.x, v.y, v.z);
  endShape(CLOSE);

  // 아랫면
  beginShape();
  for (let v of bottomPoints) vertex(v.x, v.y, v.z);
  endShape(CLOSE);

  // 측면
  for (let i = 0; i < sides; i++) {
    let next = (i + 1) % sides;
    beginShape();
    vertex(topPoints[i].x, topPoints[i].y, topPoints[i].z);
    vertex(bottomPoints[i].x, bottomPoints[i].y, bottomPoints[i].z);
    vertex(bottomPoints[next].x, bottomPoints[next].y, bottomPoints[next].z);
    vertex(topPoints[next].x, topPoints[next].y, topPoints[next].z);
    endShape(CLOSE);
  }
}

// 공 클래스
class Ball {
  constructor() {
    this.pos = createVector(0, -tubeHeight / 2 + 10, 0);
    this.vel = createVector(0, 0, 0);
    this.radius = 10;
  }

  update() {
    this.vel.y += gravity;
    this.vel.mult(friction);
    this.pos.add(this.vel);

    // 상하 충돌
    if (this.pos.y + this.radius > tubeHeight / 2) {
      this.pos.y = tubeHeight / 2 - this.radius;
      this.vel.y *= -restitution;
    }
    if (this.pos.y - this.radius < -tubeHeight / 2) {
      this.pos.y = -tubeHeight / 2 + this.radius;
      this.vel.y *= -restitution;
    }

    // XZ 평면에서 다각형 내부 체크
    if (!pointInPolygon(this.pos.x, this.pos.z, polygon2D)) {
      let closest = null;
      let minDist = Infinity;
      for (let i = 0; i < polygon2D.length; i++) {
        let a = polygon2D[i];
        let b = polygon2D[(i + 1) % polygon2D.length];
        let p = this.closestPointOnLine(a, b, createVector(this.pos.x, this.pos.z));
        let dist = p5.Vector.dist(p, createVector(this.pos.x, this.pos.z));
        if (dist < minDist) {
          minDist = dist;
          closest = p;
        }
      }

      // 반사
      let normal = p5.Vector.sub(createVector(this.pos.x, this.pos.z), closest).normalize();
      let v2d = createVector(this.vel.x, this.vel.z);
      let reflect2D = p5.Vector.sub(v2d, p5.Vector.mult(normal, 2 * v2d.dot(normal)));
      this.vel.x = reflect2D.x * restitution;
      this.vel.z = reflect2D.z * restitution;

      // 위치 보정
      this.pos.x = closest.x + normal.x * (this.radius + 0.1);
      this.pos.z = closest.z + normal.z * (this.radius + 0.1);
    }
  }

  closestPointOnLine(a, b, p) {
    let ab = p5.Vector.sub(b, a);
    let t = p5.Vector.sub(p, a).dot(ab) / ab.magSq();
    t = constrain(t, 0, 1);
    return p5.Vector.add(a, ab.mult(t));
  }

  display() {
    push();
    translate(this.pos.x, this.pos.y, this.pos.z);
    fill(255, 100, 100);
    noStroke();
    sphere(this.radius);
    pop();
  }
}

// 다각형 내부 판정
function pointInPolygon(x, z, polygon) {
  let inside = false;
  for (let i = 0, j = polygon.length - 1; i < polygon.length; j = i++) {
    let xi = polygon[i].x, zi = polygon[i].z;
    let xj = polygon[j].x, zj = polygon[j].z;
    let intersect = ((zi > z) != (zj > z)) &&
                    (x < (xj - xi) * (z - zi) / (zj - zi + 0.00001) + xi);
    if (intersect) inside = !inside;
  }
  return inside;
}
