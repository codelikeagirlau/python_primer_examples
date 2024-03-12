# fabric garment tuples
# Tuples are ordered collections of items, similar to lists, but their immutability makes for better data integrity
garment_patterns_available = ("midi dress", "classic tee", "oversized shirt", "shorts", "relaxed jeans", "mini skirt", "long sleeve shirt", "pinafore", "overalls", "quarter zip sweater")

### ------------------------------

# Weather fabric sets
# Sets are optimised for fast membership testing (checking if an element is present) and performing set operations like union, intersection, and difference.
summer_fabrics = {'linen', 'cotton', 'bamboo', 'chambray', 'denim', 'crepe'}
winter_fabrics =  {'wool', 'corduroy', 'fleece', 'bamboo', 'flannel', 'denim'}

# Union (all fabrics) - to add to the purchasing list
all_fabrics = summer_fabrics | winter_fabrics
print("All fabrics:", all_fabrics)

## Union using method
#all_fabrics = summer_fabrics.union(winter_fabrics)

# Intersection (common fabrics) - stock up on these at all times!!
common_fabrics = summer_fabrics & winter_fabrics
print("Fabrics suitable for both summer and winter:", common_fabrics)

## Intersection using method
#common_fabrics = summer_fabrics.intersection(winter_fabrics)

# Difference (season-specific fabrics) - buy at specific times of the year ready for the season!
summer_only = summer_fabrics - winter_fabrics
winter_only = winter_fabrics - summer_fabrics
print("Fabrics suitable only for summer:", summer_only)
print("Fabrics suitable only for winter:", winter_only)

## Difference using method
# summer_only = summer_fabrics.difference(winter_fabrics)
# winter_only = winter_fabrics.difference(summer_fabrics)

### ------------------------------

# Dictionaries
# dictionaries provide fast access to values based on their keys, and are highly efficient for looking up and associating data
summer_collection = {
	"midi dress": "linen",
	"classic tee": "cotton",
	"oversized shirt": "chambray",
	"shorts": "denim"
}


new_garment = input("Enter a garment to add (or 'done' to skip): ")
if new_garment in garment_patterns_available and new_garment != 'done':
    new_fabric = input(f"Enter the fabric for the {new_garment}: ")
    if new_fabric in summer_fabrics:
        summer_collection[new_garment] = new_fabric
        print(f"{new_fabric} {new_garment} added to the collection.")

    else:
        print("Fabric not suitable for summer.")

    
# Removing a garment
remove_garment = input("Enter a garment to remove (or 'done' to skip): ")
if remove_garment in summer_collection and remove_garment != 'done':
    del summer_collection[remove_garment]
    print(f"{remove_garment} removed from the collection.")

# Display final summer collection
print("\nFinal Summer Collection:")
for garment, fabric in summer_collection.items():
    print(f" - {garment}: {fabric}")
    

## DEMONSTRATING THE CLEAR() FUNCTION
# CURRENT COLLECTION
# current_collection = summer_collection
# print(current_collection)

# CLEAR CURRENT COLLECTION
# current_collection.clear()
# print(current_collection)