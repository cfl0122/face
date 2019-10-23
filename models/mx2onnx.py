from mxnet.contrib.onnx import export_model
import os,logging
import mxnet as mx
import numpy as np

def load_module(sym_filepath, params_filepath):
    """Loads the MXNet model file and
    returns MXNet symbol and params (weights).
    Parameters
    ----------
    json_path : str
        Path to the json file
    params_path : str
        Path to the params file
    Returns
    -------
    sym : MXNet symbol
        Model symbol object
    params : params object
        Model weights including both arg and aux params.
    """
    if not (os.path.isfile(sym_filepath) and os.path.isfile(params_filepath)): # pylint: disable=no-else-raise
        raise ValueError("Symbol and params files provided are invalid")
    else:
        try:
            # reads symbol.json file from given path and
            # retrieves model prefix and number of epochs
            model_name = sym_filepath.rsplit('.', 1)[0].rsplit('-', 1)[0]
            params_file_list = params_filepath.rsplit('.', 1)[0].rsplit('-', 1)
            # Setting num_epochs to 0 if not present in filename
            num_epochs = 0 if len(params_file_list) == 1 else int(params_file_list[1])
        except IndexError:
            logging.info("Model and params name should be in format: "
                         "prefix-symbol.json, prefix-epoch.params")
            raise

        sym, arg_params, aux_params = mx.model.load_checkpoint(model_name, num_epochs)

        # Merging arg and aux parameters
        params = {}
        params.update(arg_params)
        params.update(aux_params)

        return sym, params



sym = './model-symbol.json'
params = './model-0000.params'

sym,params = load_module(sym,params)
input_shape = [(1,3,112,112)]
export_model(sym,params,input_shape)




