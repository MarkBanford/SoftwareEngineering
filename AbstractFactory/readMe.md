**Abstract Factory is a creational design pattern that lets you produce families of related objects without specifying 
their concrete classes.**


1.Imagine that you are creating a furniture shop simulator. The code should consist of classes that can deal with:

    - Family of related products, say: Chair, Sofa, CoffeeTable
    - Variants of these, say Modern, Victorian, ArtDeco


2. We need to find a way to create individual furniture objects so that they match other objects of the same family. 
   Customers get quite mad when they receive non-matching furniture.
3. We also need to handle the case of when furniture vendors update their catalogs, so we shouldn't change base code.

<img src="C:\Users\markb\PycharmProjects\SoftwareEngineering\AbstractFactory\Screenshot 2022-06-18 154240.jpg"/>



**SOLUTION**

The first thing the Abstract Factory pattern suggests is to explicitly declare interfaces for each distinct product of 
the product family 
(e.g., chair, sofa or coffee table). Then you can make all variants of products follow those interfaces. 
For example, all chair variants can implement the Chair interface; all coffee table variants can implement the 
CoffeeTable interface etc

Now, how about the product variants? For each variant of a product family, we create a separate factory class based on 
the AbstractFactory 
interface. A factory is a class that returns products of a particular kind. For example, the ModernFurnitureFactory can 
only create ModernChair, ModernSofa and ModernCoffeeTable objects.