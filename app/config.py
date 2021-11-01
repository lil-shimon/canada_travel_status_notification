from dotenv import load_dotenv
import os

load_dotenv()
LINE_API = os.getenv('LINE_API')

STATUS = "● カナダ全土＝レベル3：渡航は止めてください"
DESCRIPTION = "COVID-19ワクチン接種を完了した渡航者は、入国制限の免除対象とされます。"