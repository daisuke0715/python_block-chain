
# ----------------下準備----------------
# ログを表示させるライブラリ
import logging
import sys
import utils
import hashlib
import json

logging.basicConfig(level=logging.INFO, stream=sys.stdout)

# ----------------下準備----------------

# timestampを生成するためのライブラリ
import time


# ----------------------------------------------------------
# ブロックチェーンクラス

# クラスのオブジェクトって何者？
# => インスタンス化された時に入れるやつか...
class BlockChain(object):
    # __init__関数って何者？
    def __init__(self):
        # 空のリストでtransationの情報が入るところ
        self.transation_pool = []
        # ブロックチェーンが入るリスト
        self.chain = []
        # ブロックチェーンを立ち上げた時の一番初めのブロックを生成する
        self.create_block(0, self.hash({}))

    # ブロックを作るメソッドを作る
    def create_block(self, nonce, previous_hash):
        # 単体のブロックを作成
        # ソートされたディクショナリーを生成するために sorted_dict_by_key
        block = utils.sorted_dict_by_key({
            'timestamp': time.time(),
            'transatcions': self.transation_pool,
            'nonce': nonce,
            'previous_hash': previous_hash
        })

        self.chain.append(block)
        self.transatcion_pool = []
        return block

    # ハッシュの生成
    def hash(self, block):
        # json使ってstringにキャストするときもソートすることができる
        # 上で sorted_dict_by_key でソートされているけれど、それがソートされているかどうかはhashのところではわからない
        # ダブルチェックという意味合いでさらにソートする
        # 文字列にするときはjson.dumpsで文字列にする、それに対するsorted_keyというオプションをTrueにすると文字列にするときにソートしてくれる
        sorted_block = json.dumps(block, sort_keys=True)
        return hashlib.sha256(sorted_block.encode()).hexdigest()

# ----------------------------------------------------------


# コンソールが見にくいので見やすいように変換する関数を作成
def pprint(chains):
    for i, chain in enumerate(chains):
        print(f'{"="*25} Chain {i} {"="*25}')
        for k,v in chain.items():
            print(f'{k:15}{v}')
    print(f'{"*"*25}')




# ブロックチェーンを呼び出す
if __name__ == '__main__':
    # 上記で作成したクラスをインスタンス化
    block_chain = BlockChain()
    pprint(block_chain.chain)

    # 最初のチェーンに対してもう１つブロックつけてみる
    previous_hash = block_chain.hash(block_chain.chain[-1])
    block_chain.create_block(5, previous_hash)
    pprint(block_chain.chain)

    previous_hash = block_chain.hash(block_chain.chain[-1])
    block_chain.create_block(2, previous_hash)
    pprint(block_chain.chain)










