# 파일 이름이 저장된 리스트에서 확장자가 .h나 .c인 파일을 화면에 출력하라.
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in 리스트:
    if i.endswith('.h'):
        print(i)
    elif i.endswith('.c'):
        print(i)
