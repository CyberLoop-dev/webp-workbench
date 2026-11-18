import tempfile
import unittest
from pathlib import Path
from PIL import Image
from main import convert

class ConversionTests(unittest.TestCase):
    def test_png_conversion_resizes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); source=root/"sample.png"
            Image.new("RGB",(40,20),"teal").save(source)
            output=convert(source,root/"out","png",82,25)
            with Image.open(output) as image: self.assertEqual(image.size,(25,13))

if __name__=="__main__": unittest.main()
