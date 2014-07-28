# Be sure to restart your server when you modify this file.

# Version of your assets, change this if you want to expire all your assets.
Rails.application.config.assets.version = '1.0'

# Precompile additional assets.
# application.js, application.css, and all non-JS/CSS in app/assets folder are already added.
# Rails.application.config.assets.precompile += %w( search.js )

Rails.application.config.assets.precompile += %w( proteins.js )
Rails.application.config.assets.precompile += %w( traveling_salesmen.js )
Rails.application.config.assets.precompile += %w( metalics.js )
Rails.application.config.assets.precompile += %w( metallicscanvas.js )
Rails.application.config.assets.precompile += %w( statics.js )