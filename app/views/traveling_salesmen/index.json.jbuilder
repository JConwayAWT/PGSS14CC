json.array!(@traveling_salesmen) do |traveling_salesman|
  json.extract! traveling_salesman, :id
  json.url traveling_salesman_url(traveling_salesman, format: :json)
end
