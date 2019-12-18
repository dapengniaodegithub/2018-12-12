import os
from h import main
pid=os.fork()

if pid<0:
    print("Create process failed")
elif pid==0:
    print("The new process")
    main(("0.0.0.0", 8888))
else:
    print("The old process")
    main(("0.0.0.0", 9999))
print("fork test over")