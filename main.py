#this is the to do app


import time 

def add_task():
    pass

def show_task():
    pass


def mark_task():
    pass






def main():
    is_running = True
    
    while is_running:
        print("------Welcome to the to do app!------   ")
        print("1. Add task")
        print("2. show task")
        print("3. Mark task as done")
        print("4. Exit")
        choice = input("Choose the options (1-4): ")
        
        if choice == '1':
            add_task()
        elif choice == '2':
            show_task()
        elif choice == '3':
            mark_task()
        elif choice == '4':
            is_running = False
        else:
            print("Invalid choice!!--Choose from(1-4)")
            main()
            
    time.sleep(2)        
    print("You closed this app")
            
if __name__ == "__main__":
    main()
    
    
            
            
