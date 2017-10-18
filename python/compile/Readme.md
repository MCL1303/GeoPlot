To compile `*.prim` files (primitive proto) run `python Compiler.py $in_file $out_file [$python_out_file]`

Rules of primitive proto:
  **one** file -- **one** message
  **basename** of file -- **name** of message
  **one** line -- **one** field

Features of primitive proto:
  _auto_ imports
  _bind_ fields

In `*.proto` out:
  everything is **optional**
  everything is **string**
    (except **bool**)

Syntax of line:
  $type ($name_in_python) [& $bind_type1 ($name_in_python1) [& $bind_type2 ($name_in_python2) & ...]] $name [= $default]
