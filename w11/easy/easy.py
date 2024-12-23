#!/usr/bin/env python3

import ezgmail, os

os.chdir('../output')

# Q1.宛先を自分のメールアドレス（学籍番号）に設定しよう
recipient = '???@akita-pu.ac.jp'
subject = '[ta_pp2_easy]Test mail'
body = '実行確認用のメールです'
cc = None
bcc = None
attachments = None

# Q2.送信メールに必要な変数を引数に与えよう
ezgmail.send(
    ???,
    ???,
    ???,
)

print('テスト用のメールを送信しました')

text = 'Test'
# Q3.検索するためのメソッドを呼び出そう
# Q4.検索対象に指定する情報を定義しよう
results = ezgmail.???(f'subject:{???}', maxResults=3)
for threads in results:
    # Q5.GmailThreadオブジェクトからmessages属性を取得しよう
    for email in threads.???:
        print('=====')
        # Q6.件名と差出人名を取得しよう
        print(f'件名:{email.???}, 差出人：{email.???}')
