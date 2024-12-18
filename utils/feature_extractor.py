def extract_features(pr_data, start_date, end_date):
    """PRデータから特徴量を抽出"""
    metrics_list = []
    objective_list = []

    # 仮の実装（実際のロジックに置き換え）
    for pr in pr_data:
        metrics_list.append([len(pr.get('messages', [])),  # メッセージ数
                             pr.get('lines_inserted', 0), # 追加行数
                             pr.get('lines_deleted', 0)]) # 削除行数
        objective_list.append(1 if 'reviewed' in pr else 0)

    return metrics_list, objective_list
