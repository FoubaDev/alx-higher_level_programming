#include <Python.h>
#include <stdio.h>
#include <object.h>
#include <listobject.h>

/*
 * print_python_list_info - Prints info from a given list
 * @p - A python object
 * Return None 
 */

void print_python_list_info(PyObject *p) {
    Py_ssize_t size = PyList_Size(p);

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (Py_ssize_t i = 0; i < size; i++) {
        PyObject *item = PyList_GetItem(p, i);
        const char *itemType = item->ob_type->tp_name;

        printf("Element %ld: %s\n", i, itemType);
    }
}
