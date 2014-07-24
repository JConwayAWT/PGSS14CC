Rails.application.routes.draw do

  resources :metalics

  resources :proteins

  match "/users/change_first_name", to: "users#change_first_name", via: :get
  resources :traveling_salesmen
  resources :users

  # The priority is based upon order of creation: first created -> highest priority.
  # See how all your routes lay out with "rake routes".

  # You can have the root of your site routed with "root"
  root 'statics#index'

  match '/hoffman', to: 'statics#hoffman', via: :get

  match '/tsp', to: 'traveling_salesmen#index', via: :get
  match '/protein', to: 'proteins#index', via: :get
  match '/metalics', to: 'metalics#index', via: :get

  match '/pose_traveling_salesman_problem', to: 'traveling_salesmen#pose_problem', via: :post
  match '/retreive_traveling_salesman_problem', to: 'traveling_salesmen#retreive_problem', via: :post
  match '/cancel_traveling_salesman_problem', to: 'traveling_salesmen#cancel', via: :post

  match '/pose_protein_problem', to: 'proteins#pose_problem', via: :post
  match '/retreive_protein_problem', to: 'proteins#retreive_problem', via: :post
  match '/cancel_protein_problem', to: 'proteins#cancel', via: :post

  match '/pose_metalic_problem', to: 'metalics#pose_problem', via: :post
  match '/retreive_metalic_problem', to: 'metalics#retreive_problem', via: :post
  match '/cancel_metalic_problem', to: 'metalics#cancel', via: :post

  # Example of regular route:
  #   get 'products/:id' => 'catalog#view'

  # Example of named route that can be invoked with purchase_url(id: product.id)
  #   get 'products/:id/purchase' => 'catalog#purchase', as: :purchase

  # Example resource route (maps HTTP verbs to controller actions automatically):
  #   resources :products

  # Example resource route with options:
  #   resources :products do
  #     member do
  #       get 'short'
  #       post 'toggle'
  #     end
  #
  #     collection do
  #       get 'sold'
  #     end
  #   end

  # Example resource route with sub-resources:
  #   resources :products do
  #     resources :comments, :sales
  #     resource :seller
  #   end

  # Example resource route with more complex sub-resources:
  #   resources :products do
  #     resources :comments
  #     resources :sales do
  #       get 'recent', on: :collection
  #     end
  #   end

  # Example resource route with concerns:
  #   concern :toggleable do
  #     post 'toggle'
  #   end
  #   resources :posts, concerns: :toggleable
  #   resources :photos, concerns: :toggleable

  # Example resource route within a namespace:
  #   namespace :admin do
  #     # Directs /admin/products/* to Admin::ProductsController
  #     # (app/controllers/admin/products_controller.rb)
  #     resources :products
  #   end
end
