#include <Python.h>

#include "quarkhash.h"

static PyObject *quark_getpowhash(PyObject *self, PyObject *args)
{
    char *output;
    PyObject *value;
#if PY_MAJOR_VERSION >= 3
    PyBytesObject *input;
#else
    PyStringObject *input;
#endif
    if (!PyArg_ParseTuple(args, "S", &input))
        return NULL;
    Py_INCREF(input);
    output = PyMem_Malloc(32);

#if PY_MAJOR_VERSION >= 3
    quark_hash((char *)PyBytes_AsString((PyObject*) input), output);
#else
    quark_hash((char *)PyString_AsString((PyObject*) input), output);
#endif
    Py_DECREF(input);
#if PY_MAJOR_VERSION >= 3
    value = Py_BuildValue("y#", output, 32);
#else
    value = Py_BuildValue("s#", output, 32);
#endif
    PyMem_Free(output);
    return value;
}

static PyMethodDef QUARKMethods[] = {
    { "getPoWHash", quark_getpowhash, METH_VARARGS, "Returns the proof of work hash using PIVX quark hash" },
    { NULL, NULL, 0, NULL }
};

#if PY_MAJOR_VERSION >= 3
static struct PyModuleDef QUARKModule = {
    PyModuleDef_HEAD_INIT,
    "pivx_quark_hash",
    "...",
    -1,
    QUARKMethods
};

PyMODINIT_FUNC PyInit_pivx_quark_hash(void) {
    return PyModule_Create(&QUARKModule);
}

#else

PyMODINIT_FUNC initpivx_quark_hash(void) {
    (void) Py_InitModule("pivx_quark_hash", QUARKMethods);
}
#endif
