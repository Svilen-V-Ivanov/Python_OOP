from unittest import main, TestCase

from project.student import Student


class StudentTest(TestCase):
    NAME = "John"

    def setUp(self) -> None:
        self.student = Student(self.NAME)

    def test__init__if_correct_values_are_given_without_courses__expect_correct_class(self):
        self.assertEqual(self.NAME, self.student.name)
        self.assertEqual({}, self.student.courses)

    def test__init__if_correct_values_are_given_with_none_courses__expect_correct_class(self):
        courses = None
        student = Student(self.NAME, courses)
        self.assertEqual(self.NAME, student.name)
        self.assertEqual({}, student.courses)

    def test__init__if_correct_values_are_given_with_courses__expect_correct_class(self):
        courses = {'a': [1], 'b': [2], 'c': [3]}
        student = Student(self.NAME, courses)
        self.assertEqual(self.NAME, student.name)
        self.assertEqual(courses, student.courses)

    def test__enroll__if_course_name_in_courses_dict__expect_updated_notes(self):
        course_name = 'a'
        courses = {'a': [1], 'b': [2], 'c': [3]}
        test_notes = [2, 3, 4]
        test_course_notes = ""
        student = Student(self.NAME, courses)
        result = student.enroll(course_name, test_notes, test_course_notes)
        expected_result = "Course already added. Notes have been updated."
        expected_notes = [1, 2, 3, 4]
        self.assertEqual(expected_result, result)
        self.assertEqual(expected_notes, student.courses[course_name])

    def test__enroll__if_course_name_not_in_courses_dict_and_course_notes_are_y__expect_updated_notes(self):
        course_name = 'd'
        courses = {'a': [1], 'b': [2], 'c': [3]}
        test_notes = [2, 3, 4]
        test_course_notes = "Y"
        student = Student(self.NAME, courses)
        result = student.enroll(course_name, test_notes, test_course_notes)
        expected_result = "Course and course notes have been added."
        expected_notes = [2, 3, 4]
        self.assertEqual(expected_result, result)
        self.assertEqual(expected_notes, student.courses[course_name])

    def test__enroll__if_course_name_not_in_courses_dict_and_course_notes_are_empty_string__expect_updated_notes(self):
        course_name = 'd'
        courses = {'a': [1], 'b': [2], 'c': [3]}
        test_notes = [2, 3, 4]
        test_course_notes = ""
        student = Student(self.NAME, courses)
        result = student.enroll(course_name, test_notes, test_course_notes)
        expected_result = "Course and course notes have been added."
        expected_notes = [2, 3, 4]
        self.assertEqual(expected_result, result)
        self.assertEqual(expected_notes, student.courses[course_name])

    def test__enroll__course_name_not_in_courses_dict_and_course_notes_are_not_y_empty_string__expect_new_notes(self):
        course_name = 'd'
        courses = {'a': [1], 'b': [2], 'c': [3]}
        test_notes = [2, 3, 4]
        test_course_notes = "T"
        student = Student(self.NAME, courses)
        result = student.enroll(course_name, test_notes, test_course_notes)
        expected_result = "Course has been added."
        expected_courses = {'a': [1], 'b': [2], 'c': [3], 'd': []}
        self.assertEqual(expected_result, result)
        self.assertEqual(expected_courses, student.courses)

    def test__add_notes__if_course_name_not_in_courses__raise_correct_error(self):
        course_name = 'e'
        courses = {'a': [1], 'b': [2], 'c': [3]}
        test_notes = [1, 2, 3]
        student = Student(self.NAME, courses)
        expected_exception = "Cannot add notes. Course not found."

        with self.assertRaises(Exception) as error:
            student.add_notes(course_name, test_notes)
        self.assertEqual(expected_exception, str(error.exception))

    def test__add_notes__if_course_name_in_courses__update_notes(self):
        course_name = 'a'
        courses = {'a': [1], 'b': [2], 'c': [3]}
        test_notes = [2, 3, 4]
        student = Student(self.NAME, courses)
        result = student.add_notes(course_name, test_notes)
        expected_result = "Notes have been updated"
        expected_notes = [1, [2, 3, 4]]
        self.assertEqual(expected_result, result)
        self.assertEqual(expected_notes, student.courses[course_name])

    def test__leave_course__if_course_name_not_in_courses__raise_correct_exception(self):
        course_name = 'd'
        courses = {'a': [1], 'b': [2], 'c': [3]}
        student = Student(self.NAME, courses)
        expected_exception = "Cannot remove course. Course not found."

        with self.assertRaises(Exception) as error:
            student.leave_course(course_name)
        self.assertEqual(expected_exception, str(error.exception))

    def test__leave_course__if_course_name__in_courses__update_courses(self):
        course_name = 'a'
        courses = {'a': [1], 'b': [2], 'c': [3]}
        student = Student(self.NAME, courses)
        expected_result = "Course has been removed"
        result = student.leave_course(course_name)
        expected_courses = {'b': [2], 'c': [3]}
        self.assertEqual(expected_result, result)
        self.assertEqual(expected_courses, student.courses)


if __name__ == '__main__':
    main()
