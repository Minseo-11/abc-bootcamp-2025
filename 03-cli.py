from dotenv import load_dotenv
from ai import get_personality_analysis

load_dotenv()

print("# 안녕하세요, 얼굴 특징을 입력해주시면 성격과 미래를 전망해드립니다.")
line = input("성격 특징: ").strip()
if not line:
    print("ERROR!: 얼굴 특징을 입력하시지 않으셨습니다.")
else:
    print("입력하신 얼굴 특징:", line) 
    print("분석 중 ...")
    result = get_personality_analysis(line)
    print("분석 완료 !")
    print(result)

# get_personality_analysis()