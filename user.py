def getUserInfo():
    inp = input('번호와 이름을 입력하세요 :')
    info = inp.split(' ')
    return {'num':info[0],'name':info[1]}

