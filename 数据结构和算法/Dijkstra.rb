class City
  attr_accessor :name, :routes

  def initialize(name)
    @name = name
    @routes = {}
    # 如果城市是Atlanta，则散列表应包含：{boston => 100, denver => 160}
  end

  def add_route(city, price_info)
    @route[city] = price_info
  end

  def dijkstra(starting_city, other_cities)
    route_from_city = {}
    route_from_city[starting_city]= [0, starting_city]
    other_cities.each do |city|
      route_from_city[city] = [Float::INFINITY, nill]
    end
    visited_cities = []
    current_city = starting_city
    
    while current_city
      visited_cities << current_city
      current_city.route.each do |city, price_info|
        if route_from_city[city][0] > price_info + route_from_city[current_city][0]
          route_from_city[city] = [price_info + route_from_city[current_city][0], current_city]
        end
    end

    current_city = nill
    cheapeast_route_from_current_city = Float::INFINITY
    route_from_city.each do |city, price_info|
      if price_info[0] < cheapeast_route_from_current_city && !visited_cities.include?(city)
        cheapeast_route_from_current_city = price_info[0]
        current_city = city
      end
    end
  end
  
  return route_from_city
end