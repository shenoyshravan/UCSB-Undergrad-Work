def perimRect(length,width):
   """ Compute perimeter of a rectangle """
   return 2*length + 2*width

def test_perimRect_1():
   assert perimRect(4,5)==18

def test_perimRect_2():
   assert perimRect(7,3)==20

def test_perimRect_3():
   assert perimRect(2.1,4.3)==pytest.approx(12.8)

def areaTriangle(base,height):
   return (base*height)/2

def test_areaTriangle_1():
  assert areaTriangle(4,5) == 10

def test_areaTriangle_1():
  assert areaTriangle(6,8) == 24

def test_areaTriangle_1():
  assert areaTriangle(8,10) == 40
