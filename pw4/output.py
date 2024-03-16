import curses

def decorate_ui_with_curses(mark_management_system):
    stdscr = curses.initscr()
    curses.curs_set(0)
    stdscr.clear()

    mark_management_system.calculate_and_sort_by_gpa()

    # Display the sorted list with GPA
    for student in mark_management_system.students:
        stdscr.addstr(f"{student.student_id}: {student.name} - GPA: {student.calculate_gpa()}\n")

    stdscr.refresh()
    stdscr.getch()
    curses.endwin()
