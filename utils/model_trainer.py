from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model(metrics_list, objective_list):
    """モデルを学習し、予測を行う"""
    model = RandomForestClassifier(random_state=42)
    model.fit(metrics_list, objective_list)

    # 仮の予測
    predictions = model.predict(metrics_list)

    # モデルを保存
    joblib.dump(model, "output/model.pkl")
    return model, predictions
