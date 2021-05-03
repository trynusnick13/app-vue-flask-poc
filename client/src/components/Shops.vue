<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>
          <a href="/" id="link">Home</a>
        </h1>
        <h2>
          Shops
        </h2>
        <hr><br><br>
<!--        <alert :message=message></alert>-->
        <button type="button" class="btn btn-success btn-sm" v-b-modal.shop-modal>Add Shop</button>
        <br><br>
        <table class="table table-hover">
          <thead>
          <tr>
            <th scope="col">Name</th>
            <th scope="col">Type</th>
            <th scope="col">Mall</th>
            <th scope="col">City</th>
            <th scope="col">District</th>
            <th></th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="(shop, index) in shops" :key="index">
            <td>{{ shop.Name }}</td>
            <td>{{ shop.Type }}</td>
            <td>{{ shop.Mall }}</td>
            <td>{{ shop.City }}</td>
            <td>{{ shop.District }}</td>
<!--            <td>-->
<!--              <span v-if="book.read">Yes</span>-->
<!--              <span v-else>No</span>-->
<!--            </td>-->
            <td>
              <div class="btn-group" role="group">
                <button
                  type="button"
                  class="btn btn-warning btn-sm"
                  v-b-modal.shop-update-modal
                  @click="editShop(shop)">
                  Update
                </button>
                <button
                  type="button"
                  class="btn btn-danger btn-sm"
                  @click="onDeleteShop(shop)">
                  Delete
                </button>
              </div>
            </td>
          </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addShopModal"
             id="shop-modal"
             title="Add a new shop"
             hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group id="form-mall-group"
                      label="Mall:"
                      label-for="form-mall-input">
          <b-form-input id="form-mall-input"
                        type="text"
                        v-model="addShopForm.Mall"
                        required
                        placeholder="Enter Mall">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-type-group"
                      label="Type:"
                      label-for="form-type-input">
          <b-form-input id="form-type-input"
                        type="text"
                        v-model="addShopForm.Type"
                        required
                        placeholder="Enter Type">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-name-group"
                      label="Name:"
                      label-for="form-name-input">
          <b-form-input id="form-name-input"
                        type="text"
                        v-model="addShopForm.Name"
                        required
                        placeholder="Enter Name">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-city-group"
                      label="City:"
                      label-for="form-city-input">
          <b-form-input id="form-city-input"
                        type="text"
                        v-model="addShopForm.City"
                        required
                        placeholder="Enter City">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-district-group"
                      label="District:"
                      label-for="form-district-input">
          <b-form-input id="form-district-input"
                        type="text"
                        v-model="addShopForm.District"
                        required
                        placeholder="Enter District">
          </b-form-input>
        </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>
    <b-modal ref="editShopModal"
             id="shop-update-modal"
             title="Update"
             hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
        <b-form-group id="form-mall-edit-group"
                      label="Mall:"
                      label-for="form-mall-edit-input">
          <b-form-input id="form-mall-edit-input"
                        type="text"
                        v-model="editForm.Mall"
                        required
                        placeholder="Enter mall">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-type-edit-group"
                      label="Type:"
                      label-for="form-type-edit-input">
          <b-form-input id="form-type-edit-input"
                        type="text"
                        v-model="editForm.Type"
                        required
                        placeholder="Enter type">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-name-edit-group"
                      label="Name:"
                      label-for="form-name-edit-input">
          <b-form-input id="form-name-edit-input"
                        type="text"
                        v-model="editForm.Name"
                        required
                        placeholder="Enter name">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-city-edit-group"
                      label="City:"
                      label-for="form-city-edit-input">
          <b-form-input id="form-name-city-input"
                        type="text"
                        v-model="editForm.City"
                        required
                        placeholder="Enter City">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-district-edit-group"
                      label="City:"
                      label-for="form-district-edit-input">
          <b-form-input id="form-name-district-input"
                        type="text"
                        v-model="editForm.District"
                        required
                        placeholder="Enter District">
          </b-form-input>
        </b-form-group>
        <b-button type="submit" variant="primary">Update</b-button>
        <b-button type="reset" variant="danger">Cancel</b-button>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios'
import Alert from './Alert'

// axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*'
export default {
  data () {
    return {
      shops: [],
      addShopForm: {
        id: '',
        Mall: '',
        Type: '',
        Name: '',
        City: '',
        District: ''
      },
      message: '',
      showMessage: false,
      editForm: {
        id: '',
        Mall: '',
        Type: '',
        Name: '',
        City: '',
        District: ''
      }
    }
  },
  components: {
    alert: Alert
  },
  methods: {
    getShops () {
      const path = 'http://localhost:5000/shops'
      axios.get(path)
        .then((res) => {
          this.shops = res.data.shops
          console.log(res.data)
        })
        .catch((error) => {
          // eslint-отключение следующей строки
          console.error(error)
        })
    },
    addShop (payload) {
      const path = 'http://localhost:5000/shops'
      axios.post(path, payload)
        .then(() => {
          this.getShops()
          this.message = 'Shop added!'
          this.showMessage = true
        })
        .catch((error) => {
          // eslint-отключение следующей строки
          console.log(error)
          this.getShops()
        })
    },
    editShop (shop) {
      // console.log('edit form = ' + shop.Name + shop.Mall)
      this.editForm = shop
      this.mallName = shop.Mall
    },
    updateShop (payload, shopID, mallName) {
      if (mallName.length === 0) {
        mallName = 'empty'
      }
      const path = `http://localhost:5000/shops/${shopID}/${mallName}`
      axios.put(path, payload)
        .then(() => {
          this.getShops()
        })
        .catch((error) => {
          // eslint-отключение следующей строки
          console.error(error)
          this.getShops()
        })
    },
    onResetUpdate (evt) {
      evt.preventDefault()
      // this.$refs.editShopModal.hide()
      this.initForm()
      this.getShops()
    },
    onSubmitUpdate (evt) {
      evt.preventDefault()
      this.$refs.editShopModal.hide()
      // let read = false
      // if (this.editForm.read[0]) read = true;
      const payload = {
        Mall: this.editForm.Mall,
        Type: this.editForm.Type,
        Name: this.editForm.Name,
        City: this.editForm.City,
        District: this.editForm.District
      }
      this.updateShop(payload, this.editForm.id, this.mallName)
    },
    initForm () {
      this.addShopForm.id = ''
      this.addShopForm.Mall = ''
      this.addShopForm.Type = ''
      this.addShopForm.Name = ''
      this.addShopForm.City = ''
      this.addShopForm.District = ''
      this.editForm.id = ''
      this.editForm.Name = ''
      this.editForm.Type = ''
      this.editForm.Mall = ''
      this.editForm.City = ''
      this.editForm.District = ''
    },
    onSubmit (evt) {
      evt.preventDefault()
      this.$refs.addShopModal.hide()
      // if (this.addShopForm.read[0]) read = true
      const payload = {
        Mall: this.addShopForm.Mall,
        Type: this.addShopForm.Type,
        Name: this.addShopForm.Name,
        City: this.addShopForm.City,
        District: this.addShopForm.District
      }
      this.addShop(payload)
      this.initForm()
    },
    onReset (evt) {
      evt.preventDefault()
      // this.$refs.addShopModal.hide()
      this.initForm()
    },
    removeShop (shopID, mallName) {
      if (mallName.length === 0) {
        mallName = 'empty'
      }
      const path = `http://localhost:5000/shops/${shopID}/${mallName}`
      axios.delete(path)
        .then(() => {
          this.getShops()
          this.message = 'Shop removed!'
          this.showMessage = true
        })
        .catch((error) => {
          // eslint-отключение следующей строки
          console.error(error)
          this.getShops()
        })
    },
    onDeleteShop (shop) {
      this.removeShop(shop.id, shop.Mall)
      console.log('want to delete')
      console.log(shop)
    }
  },
  created () {
    this.getShops()
  }
}
</script>

<style scoped>
#link {
  color: #28a745;
}
</style>
