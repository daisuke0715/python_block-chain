# ハッシュに関しての確認

import hashlib
import collections



# 便利なのでメソッド化
def sorted_dict_by_key(unsorted_dict):
    return collections.OrderedDict(sorted(unsorted_dict.items(), key=lambda d:d[0]))








# block = {'b': 2, 'a': 1}
# block2 = {'a': 1,'b': 2}


# print(hashlib.sha256(str(block).encode()).hexdigest())
# print(hashlib.sha256(str(block2).encode()).hexdigest())

# 上記の実行結果
# 46e391c4281c162dc452a58d0a756ec6568ebe3acbd9d3731d1eccc66c23d17b
# 3dffaea891e5dbadb390da33bad65f509dd667779330e2720df8165a253462b8


# プログラムで扱う時には同じディクショナリーで扱っていてもハッシュが異なってくると後々困る
# ディクショナリーの中身はキーで揃えた状態でブロックを作るようにする
# colletionsというライブラリをインポートする

# OrderedDict: 順番を保持するメソッド
# sortedのビルドインファンクションで block.items()(ディクショナリー)をkey,valueで取り出しているイメージ
# どのようにソートするかをkeyで渡せる。lambdaでdictionaryのd[0](keyの方)
# これでここでは、keyが「a」とか「b」なのでこれのOrderでSortしてくれる
# block = collections.OrderedDict(sorted(block.items(), key=lambda d:d[0]))
# block2 = collections.OrderedDict(sorted(block.items(), key=lambda d:d[0]))



# テストという文字列をエンコードして、違う文字列に変換する
# ある文字列からは必ず同じハッシュが導き出せる
# 暗号化ではなくて、ハッシュから逆に文字列にデコードできないようになっている
# print(hashlib.sha256(str(block).encode()).hexdigest())
# print(hashlib.sha256(str(block2).encode()).hexdigest())

