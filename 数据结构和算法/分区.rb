class SortableArray

  attr_reader :array

  def initialize(array)
    @array = array
  end

  def partition!(left_pointer, right_pointer)
    
    #总取最右的值作为轴
    pivot_position = right_pointer
    pivot = @array[pivot_position]

    right_pointer -= 1

    while true do
      
      while @array[left_pointer] < pivot do
        left_pointer += 1
      end

      while @array[right_pointer] > pivot do
        right_pointer -= 1
      end

      if left_pointer >= right_pointer
        break
      else
        swap(left_pointer, right_pointer)  
      end

    end

    #左指针和轴交换
    swap(left_pointer, pivot_position)
    
    return left_pointer
      
  end

  def swap(pointer_1, pointer_2)
    temp_value = @array[pointer_1]
    @array[pointer_1] = @array[pointer_2]
    @array[pointer_2] = temp_value
  end

  def quicksort!(left_index, right_index)
    #基准情形：分出的子数组长度为0或者1
    if right_index - left_index <= 0
      return
    end

    #数组分成两部分 并返回分隔用的轴的索引
    pivot_position = partition!(left_index, right_index)

    #轴左边 右边递归调用quicksort
    quicksort!(left_index, pivot_position -1)
    quicksort!(pivot_position + 1, right_index)
  end

end


array = [0, 5, 2, 1, 6, 3]
sortable_array = SortableArray.new(array)
sortable_array.quicksort!(0, array.length - 1)
p sortable_array.array