from menu import Menu
import function as fn

if __name__ == "__main__":
    # основной блок
    menuitems = [
        ("P", "Вывод данных", fn.print_all_data),
        ("A", "Добавление записи", fn.add_data),
        ("S", "Поиск", fn.search_data),
        ("D", "Удаление записи", fn.del_data),
        ("R", "Изменение номера записи", fn.edit_data),
        ("Q", "Выход", lambda: exit())]

    menu = Menu(menuitems)
    fn.clear_screen()
    menu.run('>:')