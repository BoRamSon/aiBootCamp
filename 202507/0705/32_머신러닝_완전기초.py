#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
머신러닝 완전 기초 학습
선형회귀, 로지스틱회귀, 의사결정트리, 랜덤포레스트 + 시각화
이 코드는 머신러닝의 대표적인 알고리즘을 아주 쉽게 실습할 수 있도록 구성되어 있습니다.
각 단계마다 상세한 한글 주석과 설명이 포함되어 있습니다.
"""

# =============================
# 1. 라이브러리 불러오기
# =============================
# numpy: 수치 계산, 배열 연산을 쉽게 해주는 라이브러리
# pandas: 표 형태(엑셀처럼)의 데이터 처리에 강력한 라이브러리
# matplotlib, seaborn: 데이터 시각화(그래프 그리기) 라이브러리
# sklearn: 머신러닝 알고리즘, 데이터셋, 평가 함수 제공
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_boston, load_breast_cancer, load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, mean_squared_error, r2_score
import warnings
warnings.filterwarnings('ignore')  # 경고 메시지 무시(코드 실행에 영향 없음)

# 한글 폰트 설정 (그래프에서 한글 깨짐 방지)
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

print("=== 머신러닝 완전 기초 학습 ===")
print("이 코드는 머신러닝의 주요 알고리즘들을 단계별로 학습합니다")
print()

# ============================================================================
# 1. 선형회귀분석 (Linear Regression)
# ============================================================================
print("1. 선형회귀분석")
print("=" * 50)
print("선형회귀: 연속적인 값을 예측하는 알고리즘 (예: 집값, 키, 몸무게 등)")
print("예시: 집의 방 개수로 집값을 예측하기")
print()

# (1) 데이터 준비: 보스턴 집값 데이터셋에서 방 개수만 사용
# - load_boston(): sklearn에서 제공하는 집값 데이터셋(506개 샘플)
# - X_boston: 방 개수만 추출 (2차원 배열)
# - y_boston: 집값(타겟, 정답)
boston = load_boston()  # sklearn 내장 데이터셋
X_boston = boston.data[:, 5:6]  # 5번째 열(방 개수)만 사용, 2차원 배열로 유지
# X_boston.shape = (506, 1)
y_boston = boston.target  # 집값 (단위: 천 달러)

print("보스턴 집값 데이터:")
print(f"데이터 개수: {len(X_boston)}개 (행: 샘플 수)")
print(f"특성: 방 개수 (열: 1개)")
print(f"타겟: 집값 (천 달러)")
print()

# (2) 데이터 분할: 훈련/테스트 데이터로 나누기 (8:2 비율)
# - train_test_split: 데이터를 무작위로 섞어서 80%는 학습용, 20%는 평가용으로 나눔
# - X_train, y_train: 모델이 학습할 데이터
# - X_test, y_test: 모델이 실제로 예측을 잘하는지 평가할 데이터
X_train, X_test, y_train, y_test = train_test_split(X_boston, y_boston, test_size=0.2, random_state=42)

# (3) 모델 생성 및 학습
# - LinearRegression(): 선형회귀 모델 객체 생성
# - fit(): 학습 데이터(X_train, y_train)로 모델을 학습시킴
lr = LinearRegression()  # 선형회귀 모델 객체 생성
lr.fit(X_train, y_train)  # 훈련 데이터로 모델 학습

# (4) 예측
# - predict(): 학습된 모델로 테스트 데이터(X_test)에 대해 집값 예측
y_pred_lr = lr.predict(X_test)  # 테스트 데이터로 집값 예측

# (5) 성능 평가
# - mean_squared_error: 예측값과 실제값의 차이(제곱)의 평균 (작을수록 좋음)
# - r2_score: 결정계수, 1에 가까울수록 예측이 잘 맞음
mse = mean_squared_error(y_test, y_pred_lr)  # 평균제곱오차(작을수록 좋음)
r2 = r2_score(y_test, y_pred_lr)  # 결정계수(1에 가까울수록 좋음)

print("선형회귀 결과:")
print(f"기울기(방 1개 증가 시 집값 증가량): {lr.coef_[0]:.2f}")  # 방 1개 늘면 집값이 얼마나 오르는지
print(f"절편(방이 0개일 때 집값): {lr.intercept_:.2f}")  # 방이 0개라면 집값은 얼마인지
print(f"평균제곱오차(MSE): {mse:.2f}")  # 예측이 실제와 얼마나 차이 나는지(작을수록 좋음)
print(f"결정계수(R²): {r2:.3f} (1에 가까울수록 예측이 잘 맞음)")
print()

# (6) 시각화: 산점도(실제값) + 예측선(모델)
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
# - scatter: 실제 집값 데이터(파란 점)
# - plot: 예측된 집값(빨간 선)
plt.scatter(X_test, y_test, alpha=0.6, label='실제 집값')  # 실제 데이터
plt.plot(X_test, y_pred_lr, color='red', linewidth=2, label='예측선')  # 예측 결과
plt.xlabel('방 개수')  # x축: 방 개수
plt.ylabel('집값 (천 달러)')  # y축: 집값
plt.title('선형회귀: 방 개수 vs 집값')
plt.legend()
plt.grid(True, alpha=0.3)

# (7) 수평막대차트: 모델 성능 시각화
plt.subplot(1, 2, 2)
# - barh: 수평 막대그래프 (모델별 성능 비교)
models = ['선형회귀']
scores = [r2]
colors = ['skyblue']
bars = plt.barh(models, scores, color=colors)
plt.xlabel('결정계수 (R²)')
plt.title('선형회귀 성능')
plt.xlim(0, 1)
for bar, score in zip(bars, scores):
    plt.text(bar.get_width() + 0.01, bar.get_y() + bar.get_height()/2, f'{score:.3f}', va='center')
plt.tight_layout()
plt.show()

# ============================================================================
# 2. 로지스틱회귀분석 (Logistic Regression)
# ============================================================================
print("2. 로지스틱회귀분석")
print("=" * 50)
print("로지스틱회귀: 분류 문제(정답이 0/1/2 등)에서 사용, 확률로 분류")
print("예시: 꽃의 특성으로 특정 종류인지 아닌지 분류하기")
print()

# (1) 데이터 준비: 아이리스 데이터에서 처음 2개 특성만 사용
# - load_iris(): sklearn 내장 꽃 데이터셋(150개 샘플, 3종류)
# - X_iris: 꽃받침 길이, 꽃받침 너비만 사용(2차원)
# - y_iris: 0번 종류(=setosa)인지 아닌지(이진분류)
iris = load_iris()
X_iris = iris.data[:, :2]  # 꽃받침 길이, 꽃받침 너비만 사용
# y_iris: 0번 종류(=setosa)인지 아닌지(이진분류)
y_iris = (iris.target == 0).astype(int)

print("아이리스 꽃 분류 데이터:")
print(f"데이터 개수: {len(X_iris)}개 (샘플 수)")
print(f"특성: 꽃받침 길이, 꽃받침 너비 (2개)")
print(f"타겟: 0번 종류인지 아닌지 (0/1)")
print()

# (2) 데이터 분할
# - train_test_split: 80%는 학습용, 20%는 평가용
X_train, X_test, y_train, y_test = train_test_split(X_iris, y_iris, test_size=0.2, random_state=42)

# (3) 모델 생성 및 학습
# - LogisticRegression(): 로지스틱회귀 모델 객체 생성
# - fit(): 학습 데이터로 모델 학습
logistic = LogisticRegression(random_state=42)
logistic.fit(X_train, y_train)

# (4) 예측
# - predict(): 학습된 모델로 테스트 데이터 예측
y_pred_logistic = logistic.predict(X_test)
accuracy_logistic = accuracy_score(y_test, y_pred_logistic)

print("로지스틱회귀 결과:")
print(f"정확도: {accuracy_logistic:.3f} ({accuracy_logistic*100:.1f}%) (1에 가까울수록 좋음)")
print(f"계수(특성별 영향력): {logistic.coef_[0]}")  # 각 특성이 결과에 미치는 영향
print(f"절편: {logistic.intercept_[0]:.3f}")
print()

# (5) 시각화: 결정 경계(분류 경계선) + 데이터 분포
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
# - meshgrid: x, y축의 모든 조합을 만들어서 결정 경계(분류 경계선) 그림
x_min, x_max = X_iris[:, 0].min() - 0.5, X_iris[:, 0].max() + 0.5
y_min, y_max = X_iris[:, 1].min() - 0.5, X_iris[:, 1].max() + 0.5
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02), np.arange(y_min, y_max, 0.02))
Z = logistic.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, alpha=0.4)  # 결정 경계 색칠
plt.scatter(X_iris[:, 0], X_iris[:, 1], c=y_iris, alpha=0.8)  # 실제 데이터
plt.xlabel('꽃받침 길이')
plt.ylabel('꽃받침 너비')
plt.title('로지스틱회귀: 결정 경계')
plt.colorbar()

# (6) 수평막대차트: 모델 성능 시각화
plt.subplot(1, 2, 2)
models = ['로지스틱회귀']
scores = [accuracy_logistic]
colors = ['lightgreen']
bars = plt.barh(models, scores, color=colors)
plt.xlabel('정확도')
plt.title('로지스틱회귀 성능')
plt.xlim(0, 1)
for bar, score in zip(bars, scores):
    plt.text(bar.get_width() + 0.01, bar.get_y() + bar.get_height()/2, f'{score:.3f}', va='center')
plt.tight_layout()
plt.show()

# ============================================================================
# 3. 의사결정트리 (Decision Tree)
# ============================================================================
print("3. 의사결정트리")
print("=" * 50)
print("의사결정트리: 질문을 통해 분류/회귀를 수행하는 알고리즘")
print("예시: 꽃의 특성에 따라 질문을 던지며 종류를 구분")
print()

# (1) 데이터 준비: 아이리스 전체 데이터 사용
# - 4개 특성 모두 사용, 3종류 분류
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)

# (2) 모델 생성 및 학습 (트리 깊이 제한)
# - max_depth=3: 트리의 최대 깊이(질문 단계 수)를 3으로 제한
# - 과적합 방지, 해석이 쉬움
dt_classifier = DecisionTreeClassifier(max_depth=3, random_state=42)
dt_classifier.fit(X_train, y_train)

# (3) 예측 및 평가
y_pred_dt = dt_classifier.predict(X_test)
accuracy_dt = accuracy_score(y_test, y_pred_dt)

print("의사결정트리 결과:")
print(f"정확도: {accuracy_dt:.3f} ({accuracy_dt*100:.1f}%) (1에 가까울수록 좋음)")
print(f"트리 깊이(질문 단계 수): {dt_classifier.get_depth()}")
print(f"리프 노드 수(최종 분류 수): {dt_classifier.get_n_leaves()}")
print()

# (4) 특성 중요도: 어떤 특성이 분류에 중요한지
feature_importance = dt_classifier.feature_importances_
feature_names = iris.feature_names
print("특성 중요도:")
for name, importance in zip(feature_names, feature_importance):
    print(f"  {name}: {importance:.3f}")
print()

# (5) 시각화: 결정 경계, 특성 중요도, 성능
plt.figure(figsize=(15, 5))
# (a) 결정 경계 (처음 2개 특성만 사용)
plt.subplot(1, 3, 1)
X_2d = iris.data[:, :2]
dt_2d = DecisionTreeClassifier(max_depth=3, random_state=42)
dt_2d.fit(X_2d, iris.target)
x_min, x_max = X_2d[:, 0].min() - 0.5, X_2d[:, 0].max() + 0.5
y_min, y_max = X_2d[:, 1].min() - 0.5, X_2d[:, 1].max() + 0.5
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02), np.arange(y_min, y_max, 0.02))
Z = dt_2d.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, alpha=0.4)
plt.scatter(X_2d[:, 0], X_2d[:, 1], c=iris.target, alpha=0.8)
plt.xlabel('꽃받침 길이')
plt.ylabel('꽃받침 너비')
plt.title('의사결정트리: 결정 경계')
# (b) 특성 중요도 막대차트
plt.subplot(1, 3, 2)
bars = plt.barh(feature_names, feature_importance, color='orange')
plt.xlabel('중요도')
plt.title('의사결정트리 특성 중요도')
for bar, importance in zip(bars, feature_importance):
    plt.text(bar.get_width() + 0.01, bar.get_y() + bar.get_height()/2, f'{importance:.3f}', va='center')
# (c) 성능 비교
plt.subplot(1, 3, 3)
models = ['의사결정트리']
scores = [accuracy_dt]
colors = ['orange']
bars = plt.barh(models, scores, color=colors)
plt.xlabel('정확도')
plt.title('의사결정트리 성능')
plt.xlim(0, 1)
for bar, score in zip(bars, scores):
    plt.text(bar.get_width() + 0.01, bar.get_y() + bar.get_height()/2, f'{score:.3f}', va='center')
plt.tight_layout()
plt.show()

# ============================================================================
# 4. 랜덤포레스트 (Random Forest)
# ============================================================================
print("4. 랜덤포레스트")
print("=" * 50)
print("랜덤포레스트: 여러 개의 의사결정트리를 조합해서 예측하는 앙상블 알고리즘")
print("예시: 여러 전문가의 의견을 종합해서 결정하기")
print()

# (1) 데이터 준비: 유방암 데이터 (이진분류)
# - load_breast_cancer(): 569개 샘플, 30개 특성, 2개 클래스(악성/양성)
cancer = load_breast_cancer()
X_cancer = cancer.data  # 30개 특성
# X_cancer.shape = (569, 30)
y_cancer = cancer.target  # 0: 악성, 1: 양성

print("유방암 분류 데이터:")
print(f"데이터 개수: {len(X_cancer)}개 (샘플 수)")
print(f"특성 개수: {X_cancer.shape[1]}개")
print(f"클래스: 악성(0), 양성(1)")
print()

# (2) 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X_cancer, y_cancer, test_size=0.2, random_state=42)

# (3) 모델 생성 및 학습
# - n_estimators=100: 100개의 의사결정트리를 조합
# - max_depth=5: 각 트리의 최대 깊이 제한(과적합 방지)
rf_classifier = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
rf_classifier.fit(X_train, y_train)

# (4) 예측 및 평가
y_pred_rf = rf_classifier.predict(X_test)
accuracy_rf = accuracy_score(y_test, y_pred_rf)

print("랜덤포레스트 결과:")
print(f"정확도: {accuracy_rf:.3f} ({accuracy_rf*100:.1f}%) (1에 가까울수록 좋음)")
print(f"트리 개수(의사결정트리 몇 개 조합?): {rf_classifier.n_estimators}")
print(f"평균 트리 깊이: {np.mean([tree.get_depth() for tree in rf_classifier.estimators_]):.1f}")
print()

# (5) 특성 중요도 (상위 10개): 어떤 특성이 예측에 중요한지
feature_importance_rf = rf_classifier.feature_importances_
feature_names_cancer = cancer.feature_names
indices = np.argsort(feature_importance_rf)[::-1]  # 중요도 순 정렬
top_features = feature_names_cancer[indices][:10]
top_importance = feature_importance_rf[indices][:10]
print("상위 10개 중요한 특성:")
for i, (name, importance) in enumerate(zip(top_features, top_importance)):
    print(f"  {i+1:2d}. {name}: {importance:.3f}")
print()

# (6) 시각화: 특성 중요도, 성능 비교, 전체 알고리즘 비교
plt.figure(figsize=(15, 5))
# (a) 특성 중요도 (상위 10개)
plt.subplot(1, 3, 1)
bars = plt.barh(range(len(top_features)), top_importance, color='lightcoral')
plt.yticks(range(len(top_features)), top_features)
plt.xlabel('중요도')
plt.title('랜덤포레스트 특성 중요도 (상위 10개)')
for i, (bar, importance) in enumerate(zip(bars, top_importance)):
    plt.text(bar.get_width() + 0.001, bar.get_y() + bar.get_height()/2, f'{importance:.3f}', va='center', fontsize=8)
# (b) 성능 비교
plt.subplot(1, 3, 2)
models = ['랜덤포레스트']
scores = [accuracy_rf]
colors = ['lightcoral']
bars = plt.barh(models, scores, color=colors)
plt.xlabel('정확도')
plt.title('랜덤포레스트 성능')
plt.xlim(0, 1)
for bar, score in zip(bars, scores):
    plt.text(bar.get_width() + 0.01, bar.get_y() + bar.get_height()/2, f'{score:.3f}', va='center')
# (c) 전체 알고리즘 성능 비교
plt.subplot(1, 3, 3)
all_models = ['선형회귀', '로지스틱회귀', '의사결정트리', '랜덤포레스트']
all_scores = [r2, accuracy_logistic, accuracy_dt, accuracy_rf]
all_colors = ['skyblue', 'lightgreen', 'orange', 'lightcoral']
bars = plt.barh(all_models, all_scores, color=all_colors)
plt.xlabel('성능 점수')
plt.title('전체 알고리즘 성능 비교')
plt.xlim(0, 1)
for bar, score in zip(bars, all_scores):
    plt.text(bar.get_width() + 0.01, bar.get_y() + bar.get_height()/2, f'{score:.3f}', va='center')
plt.tight_layout()
plt.show()

# ============================================================================
# 5. 학습 정리
# ============================================================================
print("5. 학습 정리")
print("=" * 50)
print("이 코드를 통해 머신러닝의 대표 알고리즘을 모두 경험했습니다!")
print()
print("학습한 알고리즘들:")
print("1. 선형회귀 (Linear Regression): 연속적인 값 예측 (집값, 온도 등)")
print("   - 직선으로 관계를 표현, 결정계수(R²)로 성능 평가")
print("2. 로지스틱회귀 (Logistic Regression): 분류 문제 (0/1)")
print("   - 확률을 기반으로 분류, 정확도로 성능 평가")
print("3. 의사결정트리 (Decision Tree): 질문을 통해 분류/회귀")
print("   - 이해하기 쉬운 구조, 과적합 위험 있음")
print("4. 랜덤포레스트 (Random Forest): 여러 트리 조합")
print("   - 과적합 위험이 적고, 특성 중요도 제공")
print()
print("성능 비교:")
print(f"  선형회귀 (R²): {r2:.3f}")
print(f"  로지스틱회귀 (정확도): {accuracy_logistic:.3f}")
print(f"  의사결정트리 (정확도): {accuracy_dt:.3f}")
print(f"  랜덤포레스트 (정확도): {accuracy_rf:.3f}")
print()
print("머신러닝의 핵심 개념:")
print("- 데이터로부터 패턴을 학습")
print("- 새로운 데이터에 대해 예측")
print("- 적절한 알고리즘 선택이 중요")
print("- 성능 평가와 모델 개선이 필수")
print()
print("=== 머신러닝 완전 기초 학습 완료! ===")
print("이제 머신러닝의 주요 알고리즘들을 이해했습니다!")
print("다음 단계로는 딥러닝이나 고급 기법들을 학습해보세요.") 