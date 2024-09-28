#include <Python.h>

void print_python_string(PyObject *p)
{
    if (!PyUnicode_Check(p))
    {
        printf("[.] string object info\n");
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    Py_ssize_t length;
    const char *value = PyUnicode_AsUTF8AndSize(p, &length);

    printf("[.] string object info\n");
    printf("  type: %s\n", PyUnicode_IS_COMPACT_ASCII(p) ? "compact ascii" : "compact unicode object");
    printf("  length: %zd\n", length);
    printf("  value: %s\n", value);
}
