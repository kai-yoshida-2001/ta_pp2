#!/usr/bin/env python3

from datetime import datetime, timedelta, timezone

# datetimeクラス
# Q1.今の日時情報を取得しよう
now = datetime.???()
print(f'今日は{now}です')
print(f'今日は{now.strftime("%Y-%m-%d %H:%M:%S")}')
# Q2.年の情報だけを取得して表示させよう
print(f'今日は{now.???}年です')
# Q3.月の情報だけを取得して表示させよう
print(f'今日は{now.???}月です')
# Q4.日の情報だけを取得して表示させよう
print(f'今日は{now.???}日です')
# Q5.曜日の情報だけを取得して表示させよう
print(f'今日は{now.???()}曜日です')

# timedeltaクラス
# Q6.今日から10日後の日付を計算しよう
future_date = now ? timedelta(???=10)
# Q7.10日後の月と日付の情報を出力させよう
print(f'今日から10日後は，{future_date.???}月{future_date.???}日です')

# Q8.今日から1週間前の日付を計算しよう
past_date = now ? timedelta(???=1)
# Q9.1週間前の月と日付の情報を出力させよう
print(f'今日から1週間前は，{past_date.???}月{past_date.???}日です')

# timezoneクラス
JST = timezone(timedelta(hours=+9))
print(JST)
