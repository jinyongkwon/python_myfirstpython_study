if __name__ == '__main__':
    invite_dinner = ['a', 'b', 'c']
    print(f"{invite_dinner[0]}이 불참했습니다.")
    invite_dinner[0] = 'd'
    print(f"{invite_dinner}를 초대합니다.")
    print(f"{invite_dinner}에게 알림 -  더 큰 식탁을 발견했습니다.")
    invite_dinner.insert(0, 'e')
    invite_dinner.insert(2, 'f')
    invite_dinner.append('g')
    print(f"{invite_dinner}를 초대합니다")
    print("저녁식사에는 2명밖에 올수가 없습니다.")
    pop = invite_dinner.pop()
    print(f"{pop}은 저녁에 초대하지 못해 미안합니다")
    pop = invite_dinner.pop()
    print(f"{pop}은 저녁에 초대하지 못해 미안합니다")
    pop = invite_dinner.pop()
    print(f"{pop}은 저녁에 초대하지 못해 미안합니다")
    pop = invite_dinner.pop()
    print(f"{pop}은 저녁에 초대하지 못해 미안합니다")
    print(f"{invite_dinner}는 아직 저녁 약속이 유효합니다")
    del invite_dinner[1]
    del invite_dinner[0]
    print(f"{invite_dinner}아무도 남지 않았습니다.")
