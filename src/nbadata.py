# nab-apiとやり取りをして, nba-apiで得られたデータを使いやすい形に加工し返す
# api.pyから呼ばれ, api.pyで返したデータがDBに保存される


from nba_api.stats.static import players, teams
