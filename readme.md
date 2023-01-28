# RowMapper Generate

## Steps:

1. Update the hard-coded object name in main.py to the appropriate object name.

```
objectName = "nrSchedule"
```

2. Paste the list of the entity properties including their datatype into the _rowmap.txt_ text file as such:

```
Long itemId
String identifier
Date lastUpdateDate
... etc.
```

3. Similarly, update the list of column names in the _columns.txt_ file. Ensure that you maintain the exact same order relative to the _rowmap.txt_ file, as well as keeping the surrounding quotation marks. ex:

```
"ITEM_ID"
"IDENTIFIER"
"LAST_UPDATE_DATE"
```

4. Run the program and the rowmapper contents will be wrote onto the _output.txt_ file.
