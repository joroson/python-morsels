This week we're going to normalize CSV files by writing a program, fix_csv.py, that turns a pipe-delimited file into a comma-delimited file. I'll explain how it should work by example.

Your original file will look like this:

```
Reading|Make|Model|Type|Value
Reading 0|Toyota|Previa|distance|19.83942
Reading 1|Dodge|Intrepid|distance|31.28257
```

You'll then run your script by typing this at the command line:

```
python fix_csv.py cars-original.csv cars.csv
```

Your fixed file should then look like this:

```
Reading,Make,Model,Type,Value
Reading 0,Toyota,Previa,distance,19.83942
Reading 1,Dodge,Intrepid,distance,31.28257
```

Note that it's valid for a comma to be in your input data, but you'll need to surround data cells with commas in them by double quotes when writing your output file.

It's also valid for a quote character to be in your input (you'll need to double up quotes because that's how CSV escaping works.
