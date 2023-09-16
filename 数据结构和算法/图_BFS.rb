class Person

	attr_accessor :name, :friends, :visited
	
	def initialize(name)
		@name = name
		@friends = []
		@visited = false
	end
	
	def add_friend(friend)
		@friends << friend
	end
	
	def display_network
	"""广度更新算法"""
		to_reset = [self]
		
		queue = [self]
		self.visited = true
		
		while queue.any?
			current_vertex.friends.each do |friend|
				if !friend.visited
					to_reset << friend
					queue << friend
					friend.visited = true
				end
			end
		end
	
		to_reset.each do |node|
			node.visited = false
		end
	end
	
end

mary = Person.new("Mary")
peter = Person.new("Peter")

mary.add_friend(peter)
peter.add_friend(mary)
p peter