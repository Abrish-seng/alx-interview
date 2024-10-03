def pascal_triangle(n):
  """
  This function generates a list of lists representing Pascal's Triangle of size n.

  Args:
      n: An integer representing the number of rows in the Pascal's Triangle.

  Returns:
      A list of lists containing the elements of Pascal's Triangle.
      Returns an empty list if n <= 0.
  """

  if n <= 0:
    return []

  triangle = []
  # First row is always [1]
  triangle.append([1])

  # Iterate for subsequent rows
  for i in range(1, n):
    previous_row = triangle[i-1]
    current_row = []

    # First and last elements of each row are always 1
    current_row.append(1)

    # Calculate elements in the middle
    for j in range(1, i):
      current_row.append(previous_row[j-1] + previous_row[j])

    # Add the last element (always 1)
    current_row.append(1)

    # Append the current row to the triangle
    triangle.append(current_row)

  return triangle