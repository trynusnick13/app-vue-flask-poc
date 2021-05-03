<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>
          <a href="/" id="link">Home</a>
        </h1>
        <h2>
          Malls
        </h2>
        <hr><br><br>
        <!--        <alert :message=message></alert>-->
        <button type="button" class="btn btn-success btn-sm" v-b-modal.mall-modal>Add Mall</button>
        <br><br>
        <table class="table table-hover">
          <thead>
          <tr>
            <th scope="col">Name</th>
            <th scope="col">City</th>
            <th scope="col">District</th>
            <th></th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="(mall, index) in malls" :key="index">
            <td>{{ mall.Name }}</td>
            <td>{{ mall.City }}</td>
            <td>{{ mall.District }}</td>
            <td>
              <div class="btn-group" role="group">
                <button
                  type="button"
                  class="btn btn-warning btn-sm"
                  v-b-modal.mall-update-modal
                  @click="editMall(mall)">
                  Update
                </button>
                <button
                  type="button"
                  class="btn btn-danger btn-sm"
                  @click="onDeleteMall(mall)">
                  Delete
                </button>
              </div>
            </td>
          </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addMallModal"
             id="mall-modal"
             title="Add a new mall"
             hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group id="form-name-group"
                      label="Name:"
                      label-for="form-name-input">
          <b-form-input id="form-name-input"
                        type="text"
                        v-model="addMallForm.Name"
                        required
                        placeholder="Enter Name">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-city-group"
                      label="City:"
                      label-for="form-city-input">
          <b-form-input id="form-city-input"
                        type="text"
                        v-model="addMallForm.City"
                        required
                        placeholder="Enter City">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-district-group"
                      label="District:"
                      label-for="form-district-input">
          <b-form-input id="form-district-input"
                        type="text"
                        v-model="addMallForm.District"
                        required
                        placeholder="Enter District">
          </b-form-input>
        </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>
    <b-modal ref="editMallModal"
             id="mall-update-modal"
             title="Update"
             hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
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
      malls: [],
      addMallForm: {
        id: '',
        Name: '',
        City: '',
        District: ''
      },
      message: '',
      showMessage: false,
      editForm: {
        id: '',
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
    getMalls () {
      const path = 'http://localhost:5000/malls'
      axios.get(path)
        .then((res) => {
          this.malls = res.data.malls
          console.log(res.data)
        })
        .catch((error) => {
          // eslint-отключение следующей строки
          console.error(error)
        })
    },
    addMall (payload) {
      const path = 'http://localhost:5000/malls'
      axios.post(path, payload)
        .then(() => {
          this.getMalls()
          this.message = 'Mall added!'
          this.showMessage = true
        })
        .catch((error) => {
          // eslint-отключение следующей строки
          console.log(error)
          this.getMalls()
        })
    },
    editMall (mall) {
      // console.log('edit form = ' + mall.Name + mall.Mall)
      this.editForm = mall
    },
    updateMall (payload, mallID) {
      const path = `http://localhost:5000/malls/${mallID}`
      axios.put(path, payload)
        .then(() => {
          this.getMalls()
        })
        .catch((error) => {
          // eslint-отключение следующей строки
          console.error(error)
          this.getMalls()
        })
    },
    onResetUpdate (evt) {
      evt.preventDefault()
      // this.$refs.editMallModal.hide()
      this.initForm()
      this.getMalls()
    },
    onSubmitUpdate (evt) {
      evt.preventDefault()
      this.$refs.editMallModal.hide()
      // let read = false
      // if (this.editForm.read[0]) read = true;
      const payload = {
        Name: this.editForm.Name,
        City: this.editForm.City,
        District: this.editForm.District
      }
      this.updateMall(payload, this.editForm.id)
    },
    initForm () {
      this.addMallForm.id = ''
      this.addMallForm.Name = ''
      this.addMallForm.City = ''
      this.addMallForm.District = ''
      this.editForm.id = ''
      this.editForm.Name = ''
      this.editForm.City = ''
      this.editForm.District = ''
    },
    onSubmit (evt) {
      evt.preventDefault()
      this.$refs.addMallModal.hide()
      // if (this.addMallForm.read[0]) read = true
      const payload = {
        Name: this.addMallForm.Name,
        City: this.addMallForm.City,
        District: this.addMallForm.District
      }
      this.addMall(payload)
      this.initForm()
    },
    onReset (evt) {
      evt.preventDefault()
      // this.$refs.addMallModal.hide()
      this.initForm()
    },
    removeMall (mallID) {
      const path = `http://localhost:5000/malls/${mallID}`
      axios.delete(path)
        .then(() => {
          this.getMalls()
          this.message = 'Mall removed!'
          this.showMessage = true
        })
        .catch((error) => {
          // eslint-отключение следующей строки
          console.error(error)
          this.getMalls()
        })
    },
    onDeleteMall (mall) {
      this.removeMall(mall.id)
    }
  },
  created () {
    this.getMalls()
  }
}
</script>

<style scoped>
#link {
  color: #28a745;
}
</style>
