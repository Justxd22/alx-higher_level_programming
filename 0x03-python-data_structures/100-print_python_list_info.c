#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - print info about P (list)
 * @p: list to print info about
 *
 * No Return
**/
void print_python_list_info(PyObject *p)
{
        PyListObject *list = (PyListObject *)p;
        Py_ssize_t s = PyList_Size(p), alloc = list->allocated, x;
        PyObject *item;

        printf("[*] Size of the Python List = %ld\n", s);
        printf("[*] Allocated = %ld\n", alloc);
        for (x = 0; x < s; x++)
        {
                item = PyList_GetItem(p, x);
                printf("Element %ld: %s\n", x, Py_TYPE(item)->tp_name);
        }

}