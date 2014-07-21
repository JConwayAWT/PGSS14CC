json.array!(@metalics) do |metalic|
  json.extract! metalic, :id
  json.url metalic_url(metalic, format: :json)
end
