#!/usr/bin/env python3

import ezgmail, os
from datetime import datetime, timedelta
from collections import defaultdict

os.chdir('../output')

seven_days_ago = datetime.now() - timedelta(days=7)

query = f"after:{seven_days_ago.strftime('%Y/%m/%d')}"
# Q1.'query'を引数に与えることで，目的のメール情報だけを取得しよう
threads = ezgmail.search(query)

sender_counts = defaultdict(int)
longest_subject = {"length": 0, "subject": "", "sender": ""}
report_count = 0

for thread in threads:
    # Q2.すべてのメールメッセージのリストを定義しよう
    for message in thread.messages:
        message_date = message.timestamp.date()
        if message_date >= seven_days_ago.date():
            # Q3.メールメッセージの送信者のメールアドレスを取得しよう
            sender_counts[message.sender] += 1
            # Q4.メールメッセージの件名を取得しよう
            if len(message.subject) > longest_subject["length"]:
                longest_subject = {
                    "length": len(message.subject),
                    # Q5.メールメッセージの件名を取得しよう
                    "subject": message.subject,
                    # Q6.メールメッセージの送信者のメールアドレスを取得しよう
                    "sender": message.sender,
                }
            # Q7.メールメッセージの件名を取得しよう
            if "Test" in message.subject:
                report_count += 1

print("送信者ごとのメール数:")
for sender, count in sender_counts.items():
    print(f"{sender}: {count}件")

print("\n最も件名が長いメール:")
print(f"件名: {longest_subject['subject']}")
print(f"送信者: {longest_subject['sender']}")

print("\n件名に「Test」を含むメールの件数:")
print(f"{report_count}件")
