#include <Python.h>

int Cfib(int n){
    if (n<2){
        return n;
    }
    else{
        return Cfib(n-1) + Cfib(n-2);
    }
}

static PyObject* fib(PyObject* self, PyObject* args)
{
    int n;
    if(!PyArg_ParseTuple(args, "i", &n)){
        return NULL;
    }
    else{
        return Py_BuildValue("i", Cfib(n));
    }
}

static PyObject* version(PyObject* self)
{
    return Py_BuildValue("s", "Version 1.0");
}

static PyMethodDef myMethods[] = {
    {"fib", fib, METH_VARARGS, "Calculate the Fibonacci number."},
    {"version", (PyCFunction)version, METH_NOARGS, "Return the version."},
    {NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC initmyModule(void){
    (void) Py_InitModule("myModule", myMethods);
}
