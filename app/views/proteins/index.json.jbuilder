json.array!(@proteins) do |protein|
  json.extract! protein, :id
  json.url protein_url(protein, format: :json)
end
