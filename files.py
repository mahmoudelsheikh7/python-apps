def op2(the_file_1):
    n = 1
    while n == 1:
        try:
            user_d = int(input("\n (1) open file \n (2) rewrite file content\n (3) add to file \n (4) main menu \n (5) exit \n : "))
            if user_d == 1:
                file_read(the_file_1)
            elif user_d == 2:
                file_write(the_file_1)
                file_read(the_file_1)
            elif user_d == 3:
                file_append(the_file_1)
                file_read(the_file_1)
            elif user_d == 4:
                op()
            elif user_d == 5:
                print("exit....(^_^)")
                print("="*30, "\n (->->->->)Made By(<-<-<-<-) \n \tMahmoud ElSheikh\n", "="*30)
                n = 0
            else:
                print("enter number from 1 to 5")
        except ValueError:
            print("enter integer number only (-_-)")
        except Exception as e:
            print("error ", e)


def file_name():
    return input("enter file name with format like (.txt): ")


def file_read(the_file_1):
    try:
        with open(the_file_1, "r") as file:
            content = file.read()
        print("current file content: \n")
        print(content)
        op2(the_file_1)
    except FileNotFoundError:
        print("file not found (^_^)")
    except Exception as e:
        print("the error: ", e)


def file_write(the_file_1):
    try:
        with open(the_file_1, "w") as file:
            mm = input("Enter content you want to write: ")
            file.write(mm)
        print("Content written to the file.")
        op2(the_file_1)
    except FileNotFoundError:
        print("file not found !")
    except Exception as e:
        print("error ! :", e)


def file_append(the_file_1):
    try:
        with open(the_file_1, "a") as file:
            content_a = input(f"enter content you want to add to the {the_file_1}: ")
            file.write(f"\n{content_a}")
        print("done")
    except FileNotFoundError:
        print("file not found !")
    except Exception as e:
        print("error: ", e)


def create_file():
    try:
        file_name_input = input("enter new file name: ")
        with open(file_name_input, "w") as file:
            content = input("enter file content: ")
            file.write(content)
        print(f"new file created with name: {file_name_input}")
        file_read(file_name_input)
    except Exception as e:
        print("error: ", e)


def op():
    n = 1
    while n == 1:
        try:
            user_d = int(input("\n (1) open file \n (2) rewrite file content\n (3) add to file \n (4) create new file \n (5) exit \n : "))
            if user_d == 1:
                the_file_1 = file_name()
                file_read(the_file_1)
            elif user_d == 2:
                the_file_1 = file_name()
                file_write(the_file_1)
                file_read(the_file_1)
            elif user_d == 3:
                the_file_1 = file_name()
                file_append(the_file_1)
                file_read(the_file_1)
            elif user_d == 4:
                create_file()
            elif user_d == 5:
                print("exit....(^_^)")
                print("=" * 30, "\n (->->->->)Made By(<-<-<-<-) \n \tMahmoud ElSheikh\n", "=" * 30)
                n = 0
            else:
                print("enter number from 1 to 5")
        except ValueError:
            print("enter integer number only (-_-)")
        except Exception as e:
            print("error ", e)


op()
