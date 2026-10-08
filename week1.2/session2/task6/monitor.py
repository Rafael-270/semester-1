# Week 1.2, Session 2: Task 6
temperature=int(input("Enter the machine's temperature in Celsius "))
pressure=int(input("Enter the machine's pressure in PSI "))
status=int(input("Enter the machine's operational status, 1 for operating, 0 for stopped "))
normal = True

if temperature > 80:
    if status == 1:
        normal = False
        print("The temperature is too high, please shut down machine")
    else:
       print("The temperature is too high, the machine is stopped, no immediate actions is needed")
elif 50 <= temperature <= 80:
  print("The temperature is within safe limits")
else:
  print("The temperature is low")

if pressure > 100:
    if status == 1:
        normal = False
        print("The pressure is too high, seek maintenance")
    else:
       print("The pressure is too high, the machine is stopped, no immediate action is needed")
elif 70 <= pressure <= 100:
   print("Pressure is stable")
else:
   print("Pressure is low, system is operating normally")

if status == 1 and normal == True:
   print("Machine is running normally")
elif normal == False:
   print("Take action")

if status == 0:
    print("Machine is not currently operating, no action needed")
