#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
기초 암 분류 - KNN 알고리즘
"""

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

print("=== 기초 암 분류 학습 ===")

# 1. 데이터 로드
cancer = load_breast_cancer()
X = cancer.data  # 특성 데이터
y = cancer.target  # 타겟 데이터 (0: 악성, 1: 양성)

print(f"데이터: {X.shape[0]}개 샘플, {X.shape[1]}개 특성")
print(f"악성: {sum(y==0)}개, 양성: {sum(y==1)}개")

# 2. 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 3. KNN 모델 만들기
knn = KNeighborsClassifier(n_neighbors=5)

# 4. 모델 훈련
knn.fit(X_train, y_train)

# 5. 예측하기
y_pred = knn.predict(X_test)

# 6. 정확도 확인
accuracy = accuracy_score(y_test, y_pred)
print(f"정확도: {accuracy:.2%}")

# 7. 간단한 예측 예시
new_data = X_test[0].reshape(1, -1)
prediction = knn.predict(new_data)[0]
print(f"새로운 데이터 예측: {'악성' if prediction == 0 else '양성'}")

print("학습 완료!") 