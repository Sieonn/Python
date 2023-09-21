#Module Search Odering
# 1. 동일 디렉토리
# 2. sys.path
# 3. PYTHONPATH = 경로를 통해서 파이썬의 환경변수를 생성하고 export해준다.
    #팀 작업을 하는데 하나의 git에 업로드 할때 
    # who
    # when
    # objective
    # Environment...
    #OS,version, Tool
    #를 작성해준다.


import sys
for path in sys.path:
    print(path)