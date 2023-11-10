#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - print bytes
 * @p: list to print info about
 *
 * No Return
**/
void print_python_bytes(PyObject *p)
{
        const char *str = PyBytes_AsString(p);      
        Py_ssize_t size = PyBytes_Size(p), i;

        printf("[.] bytes object info\n");      
        if (!PyBytes_Check(p))
        {
            printf("  [ERROR] Invalid Bytes Object\n");
            return;
        }       

        printf("  size: %zd\n", size);
        printf("  trying string: %s\n", str);       
        printf("  first %zd bytes:", size > 10 ? 10 : size);

        for (i = 0; i < (size > 10 ? 10 : size); ++i)
        {
            printf(" %02x", (unsigned char)str[i]);
        }
        printf("\n");
}


/**
 * print_python_list - print info about P (list)
 * @p: list to print info about
 *
 * No Return
**/
void print_python_list(PyObject *p)
{
        PyListObject *list = (PyListObject *)p;
        Py_ssize_t s = PyList_Size(p), alloc = list->allocated, x;
        PyObject *item;

        printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %ld\n", s);
        printf("[*] Allocated = %ld\n", alloc);
        for (x = 0; x < s; x++)
        {
                item = PyList_GetItem(p, x);
                printf("Element %ld: ", x);
                switch (Py_TYPE(item)->tp_flags)
                {
                case PyBytes_Type.tp_flags:
                    print_python_bytes(item);
                    break;
                case PyFloat_Type.tp_flags:
                    printf("float\n");
                    break;
                case PyTuple_Type.tp_flags:
                    printf("tuple\n");
                    break;
                case PyList_Type.tp_flags:
                    print_python_list(item);
                    break;
                case PyLong_Type.tp_flags:
                    printf("int\n");
                    break;
                case PyUnicode_Type.tp_flags:
                    printf("str\n");
                    break;
                default:
                    printf("%s\n", Py_TYPE(item)->tp_name);
                }   
        }   
}