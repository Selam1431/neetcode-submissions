class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        students = deque(students)
        i = 0
        skipped = 0

        while students and skipped < len(students):
            if students[0] == sandwiches[i]:
                students.popleft()
                i += 1
                skipped = 0
            else:
                students.append(students.popleft())
                skipped += 1

        return len(students)
            