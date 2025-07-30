#!/usr/bin/python
# Author: Conan Yu
# Date: 07/30/2025
# Filter pattern implement

# Version 1.0
#====================================================================
from filterFramework import Filter

class FilterScreen(Filter):
    """過濾網"""

    def doFilter(self, elements):
        for material in elements:
            if (material == "豆渣"):
                elements.remove(material)
        return elements
    
if __name__ == "__main__":
    rawMaterials = ["豆漿", "豆渣"]
    print("過濾前：", rawMaterials)
    afterFilter = FilterScreen()
    filteredMaterials = afterFilter.doFilter(rawMaterials)
    print("過濾後：",filteredMaterials)
