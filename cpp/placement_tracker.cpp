#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

struct Student {
    std::string name;
    double cgpa;
    int backlogs;
};

std::vector<Student> studentsAtRisk(const std::vector<Student>& students) {
    return {};
}

std::vector<std::string> names(const std::vector<Student>& students) {
    std::vector<std::string> result;
    for (const Student& student : students) {
        result.push_back(student.name);
    }
    return result;
}

bool expect(const std::vector<std::string>& actual,
            const std::vector<std::string>& expected,
            const std::string& label) {
    if (actual == expected) {
        return true;
    }

    std::cerr << "FAIL: " << label << "\n";
    std::cerr << "Expected:";
    for (const std::string& name : expected) {
        std::cerr << " " << name;
    }
    std::cerr << "\nActual:";
    for (const std::string& name : actual) {
        std::cerr << " " << name;
    }
    std::cerr << "\n";
    return false;
}

int main() {
    const std::vector<Student> batch = {
        {"Asha", 9.0, 0},
        {"Bhavya", 5.5, 0},
        {"Chetan", 8.0, 2},
        {"Divya", 4.2, 3},
        {"Esha", 6.0, 0},
    };

    const std::vector<Student> atRisk = studentsAtRisk(batch);
    bool allPassed = true;
    allPassed = expect(
                    names(atRisk),
                    {"Divya", "Bhavya", "Chetan"},
                    "finds and sorts at-risk students") &&
                allPassed;
    allPassed = expect(names(studentsAtRisk({})), {},
                       "handles an empty batch") &&
                allPassed;
    allPassed = expect(
                    names(studentsAtRisk({{"First", 5.5, 0},
                                          {"Second", 5.5, 1}})),
                    {"First", "Second"},
                    "preserves order for equal CGPAs") &&
                allPassed;

    if (allPassed) {
        std::cout << "ALL TESTS PASS\n";
        return 0;
    }
    return 1;
}
