# Label Generator of Grasp Detection

___

this application of label generator is based on new grasp detection annotation from our recent research. 

Run the following command to configure the environment:

```
pip install -r requirements.txt
```

You need to note that the labeled image is generated under folder ``'customdata\new_labels\'``, before running.

Run the GUI with the following command:

```python
python run_test_label.py
```

After clicking the Start button, you then need to click twice for the grasp path and again for the width of the grasp. click the Save button to save the labels after all paths are marked. It can also be re-labeled at any time by using the Re-labeling button. **Click the mouse should not be too fast, may kill the program in the annotation.**

<iframe height = 498, width = 510 src="demostration/demonstration.mp4" frameborder=0 allowfullscreen></iframe>

