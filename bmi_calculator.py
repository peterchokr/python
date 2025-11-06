"""
BMI(체질량지수) 계산기
Body Mass Index Calculator
"""

def calculate_bmi(weight, height):
    """
    BMI를 계산하는 함수

    Parameters:
    weight (float): 체중 (kg)
    height (float): 신장 (cm)

    Returns:
    float: BMI 값
    """
    # 신장을 cm에서 m로 변환
    height_m = height / 100
    # BMI 계산: 체중(kg) / (신장(m))^2
    bmi = weight / (height_m ** 2)
    return bmi


def get_bmi_category(bmi):
    """
    BMI 값에 따른 체중 분류를 반환하는 함수

    Parameters:
    bmi (float): BMI 값

    Returns:
    str: 체중 분류
    """
    if bmi < 18.5:
        return "저체중"
    elif bmi < 23:
        return "정상"
    elif bmi < 25:
        return "과체중"
    elif bmi < 30:
        return "비만"
    else:
        return "고도비만"


def main():
    """
    BMI 계산기 메인 함수
    """
    print("=" * 40)
    print("BMI(체질량지수) 계산기")
    print("=" * 40)

    try:
        # 사용자로부터 체중과 신장 입력받기
        weight = float(input("체중을 입력하세요 (kg): "))
        height = float(input("신장을 입력하세요 (cm): "))

        # 입력값 유효성 검사
        if weight <= 0 or height <= 0:
            print("체중과 신장은 0보다 커야 합니다.")
            return

        if height > 300:
            print("신장 값이 너무 큽니다. cm 단위로 입력하세요.")
            return

        # BMI 계산
        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)

        # 결과 출력
        print("\n" + "=" * 40)
        print("결과")
        print("=" * 40)
        print(f"신장: {height} cm")
        print(f"체중: {weight} kg")
        print(f"BMI: {bmi:.2f}")
        print(f"분류: {category}")
        print("=" * 40)

        # BMI 분류 기준 안내
        print("\n[BMI 분류 기준]")
        print("저체중: 18.5 미만")
        print("정상: 18.5 ~ 22.9")
        print("과체중: 23 ~ 24.9")
        print("비만: 25 ~ 29.9")
        print("고도비만: 30 이상")

    except ValueError:
        print("올바른 숫자를 입력하세요.")
    except Exception as e:
        print(f"오류가 발생했습니다: {e}")


if __name__ == "__main__":
    main()
