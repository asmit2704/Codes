def helpdesk():
    print("===== HELP DESK EXPERT SYSTEM =====")
    while True:
        print("\nSelect Problem:")
        print("1. Internet Issue")
        print("2. Slow Computer")
        print("3. Printer Issue")
        print("4. Login Problem")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("\nSolution:")
            print("1. Check WiFi connection")
            print("2. Restart router")
            print("3. Contact network administrator")
        elif choice == 2:
            print("\nSolution:")
            print("1. Close unnecessary programs")
            print("2. Delete temporary files")
            print("3. Restart computer")
        elif choice == 3:
            print("\nSolution:")
            print("1. Check printer cable")
            print("2. Check printer power")
            print("3. Install printer driver")
        elif choice == 4:
            print("\nSolution:")
            print("1. Check username and password")
            print("2. Reset password")
            print("3. Contact administrator")
        elif choice == 5:
            print("Exiting Expert System...")
            break
        else:
            print("Invalid Choice")
helpdesk()